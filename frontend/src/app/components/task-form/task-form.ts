import { Component, EventEmitter, OnInit, Output, signal } from '@angular/core';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-task-form',
  standalone: true,
  templateUrl: './task-form.html',
})
export class TaskForm implements OnInit {

  @Output() onClose = new EventEmitter<void>();
  projects = signal<any[]>([]);

  title = signal('');
  status = signal('todo');
  assignee = signal('');
  createdBy = signal('');
  projectId = signal<number | null>(null);

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.loadProjects();
  }

  loadProjects() {
    this.api.getProjects().subscribe((res: any) => {
      this.projects.set(res);
    });
  }

  createTask() {

    if (!this.title() || !this.projectId()) {
      alert("Task title and project required");
      return;
    }

    const payload = {
      title: this.title(),
      project_id: this.projectId(),
      status: this.status(),
      assignee: this.assignee(),
      created_by: this.createdBy()
    };

    this.api.createTask(payload).subscribe(() => {

      alert("Task created (AI will generate description & priority)");

      this.title.set('');
      this.assignee.set('');
      this.createdBy.set('');
      this.status.set('todo');

      this.onClose.emit();
    });

  }

}