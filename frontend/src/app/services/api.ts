import { inject, Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  http = inject(HttpClient);
  API = 'http://localhost:8000';
  constructor() { }

  getProjects() {
    return this.http.get(`${this.API}/projects`);
  }

  createProject(data: any) {
    return this.http.post(`${this.API}/projects`, data);
  }

  getTasks(params?: any) {
    return this.http.get(`${this.API}/tasks`, { params });
  }

  createTask(data: any) {
    return this.http.post(`${this.API}/tasks`, data);
  }

  getTasksByProject(projectId: number) {
    return this.http.get(`${this.API}/tasks/project/${projectId}`);
  }

  getComments(taskId: number) {
    return this.http.get(`${this.API}/comment/${taskId}/comments`);
  }

  addComment(taskId: number, data: any) {
    return this.http.post(`${this.API}/comment/${taskId}/comments`, data);
  }

  updateTaskStatus(taskId: number, status: string) {
    return this.http.patch(`${this.API}/tasks/${taskId}/status`, { status });
  }

}