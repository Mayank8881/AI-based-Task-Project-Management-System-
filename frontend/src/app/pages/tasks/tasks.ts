import { Component, OnInit, signal } from '@angular/core';
import { ApiService } from '../../services/api';
import { CommentBoxComponent } from '../../components/comment-box/comment-box';
import { TaskForm } from '../../components/task-form/task-form';

@Component({
  selector: 'app-tasks',
  imports: [CommentBoxComponent, TaskForm],
  templateUrl: './tasks.html',
  styleUrl: './tasks.css',
})
export class TasksComponent implements OnInit {

  tasks = signal<any[]>([]);
  projects = signal<any[]>([]);

  selectedProject = signal<any>('all');
  selectedPriority = signal('');
  selectedStatus = signal('');
  selectedAssignee = signal('');

  showTaskForm = signal(false);

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.loadProjects();
    this.loadTasks();
  }

  loadProjects() {
    this.api.getProjects().subscribe((res: any) => {
      this.projects.set(res);
    });
  }

  loadTasks() {

    const params: any = {};

    if (this.selectedPriority()) {
      params.priority = this.selectedPriority();
    }

    if (this.selectedStatus()) {
      params.status = this.selectedStatus();
    }

    if (this.selectedAssignee()) {
      params.assignee = this.selectedAssignee();
    }

    if (this.selectedProject() !== 'all') {

      this.api.getTasksByProject(this.selectedProject()).subscribe((res: any) => {
        this.tasks.set(res);
      });

      return;
    }

    this.api.getTasks(params).subscribe((res: any) => {
      this.tasks.set(res);
    });
  }

  onProjectChange(event: any) {
    this.selectedProject.set(event.target.value);
    this.loadTasks();
  }

  onPriorityChange(event: any) {
    this.selectedPriority.set(event.target.value);
    this.loadTasks();
  }

  onStatusChange(event: any) {
    this.selectedStatus.set(event.target.value);
    this.loadTasks();
  }

  onAssigneeChange(event: any) {
    this.selectedAssignee.set(event.target.value);
    this.loadTasks();
  }

  showComments: Record<number, boolean> = {};

  toggleComments(taskId: number) {
    this.showComments[taskId] = !this.showComments[taskId];
  }

  toggleTaskForm() {
    this.showTaskForm.set(!this.showTaskForm());
  }

  updateStatus(taskId: number, event: any) {
    const status = event.target.value;

    this.api.updateTaskStatus(taskId, status).subscribe(() => {
      this.loadTasks();
    });
  }

}