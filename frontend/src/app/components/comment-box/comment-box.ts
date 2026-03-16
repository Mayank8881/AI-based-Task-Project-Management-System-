import { Component, Input, OnInit, signal } from '@angular/core';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-comment-box',
  templateUrl: './comment-box.html',
  styleUrl: './comment-box.css',
})
export class CommentBoxComponent implements OnInit {

  @Input() taskId!: number;

  comments = signal<any[]>([]);
  commentText = signal('');
  commentedBy = signal('');

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.loadComments();
  }

  loadComments() {
    this.api.getComments(this.taskId).subscribe((res: any) => {
      this.comments.set(res);
    });
  }

  addComment() {

    if (!this.commentText() || !this.commentedBy()) {
      alert("Please fill both fields");
      return;
    }

    this.api.addComment(this.taskId, {
      comment: this.commentText(),
      commented_by: this.commentedBy()
    }).subscribe(() => {

      this.commentText.set('');
      this.commentedBy.set('');

      this.loadComments();
    });

  }
}