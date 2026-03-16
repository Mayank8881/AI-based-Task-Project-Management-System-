import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CommentBoxComponent } from './comment-box';

describe('CommentBox', () => {
  let component: CommentBoxComponent;
  let fixture: ComponentFixture<CommentBoxComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CommentBoxComponent],
    }).compileComponents();

    fixture = TestBed.createComponent(CommentBoxComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
