---
title: SimpleTreeVisitor
permalink: Java/SimpleTreeVisitor
date: 2021-01-04
key: JavaJava.S.SimpleTreeVisitor
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SimpleTreeVisitor.description }}

## Sintaxis
~~~java
public class SimpleTreeVisitor<R,P> extends Object implements TreeVisitor<R,P>
~~~

## Constructores
* [SimpleTreeVisitor()](/Java/SimpleTreeVisitor/SimpleTreeVisitor/)

## Campos
* [DEFAULT_VALUE](/Java/SimpleTreeVisitor/DEFAULT_VALUE)

## Métodos
* [defaultAction()](/Java/SimpleTreeVisitor/defaultAction)
* [visit()](/Java/SimpleTreeVisitor/visit)
* [visitAnnotatedType()](/Java/SimpleTreeVisitor/visitAnnotatedType)
* [visitAnnotation()](/Java/SimpleTreeVisitor/visitAnnotation)
* [visitArrayAccess()](/Java/SimpleTreeVisitor/visitArrayAccess)
* [visitArrayType()](/Java/SimpleTreeVisitor/visitArrayType)
* [visitAssert()](/Java/SimpleTreeVisitor/visitAssert)
* [visitAssignment()](/Java/SimpleTreeVisitor/visitAssignment)
* [visitBinary()](/Java/SimpleTreeVisitor/visitBinary)
* [visitBlock()](/Java/SimpleTreeVisitor/visitBlock)
* [visitBreak()](/Java/SimpleTreeVisitor/visitBreak)
* [visitCase()](/Java/SimpleTreeVisitor/visitCase)
* [visitCatch()](/Java/SimpleTreeVisitor/visitCatch)
* [visitClass()](/Java/SimpleTreeVisitor/visitClass)
* [visitCompilationUnit()](/Java/SimpleTreeVisitor/visitCompilationUnit)
* [visitCompoundAssignment()](/Java/SimpleTreeVisitor/visitCompoundAssignment)
* [visitConditionalExpression()](/Java/SimpleTreeVisitor/visitConditionalExpression)
* [visitContinue()](/Java/SimpleTreeVisitor/visitContinue)
* [visitDoWhileLoop()](/Java/SimpleTreeVisitor/visitDoWhileLoop)
* [visitEmptyStatement()](/Java/SimpleTreeVisitor/visitEmptyStatement)
* [visitEnhancedForLoop()](/Java/SimpleTreeVisitor/visitEnhancedForLoop)
* [visitExpressionStatement()](/Java/SimpleTreeVisitor/visitExpressionStatement)
* [visitForLoop()](/Java/SimpleTreeVisitor/visitForLoop)
* [visitIdentifier()](/Java/SimpleTreeVisitor/visitIdentifier)
* [visitIf()](/Java/SimpleTreeVisitor/visitIf)
* [visitImport()](/Java/SimpleTreeVisitor/visitImport)
* [visitInstanceOf()](/Java/SimpleTreeVisitor/visitInstanceOf)
* [visitIntersectionType()](/Java/SimpleTreeVisitor/visitIntersectionType)
* [visitLabeledStatement()](/Java/SimpleTreeVisitor/visitLabeledStatement)
* [visitLambdaExpression()](/Java/SimpleTreeVisitor/visitLambdaExpression)
* [visitLiteral()](/Java/SimpleTreeVisitor/visitLiteral)
* [visitMemberReference()](/Java/SimpleTreeVisitor/visitMemberReference)
* [visitMemberSelect()](/Java/SimpleTreeVisitor/visitMemberSelect)
* [visitMethod()](/Java/SimpleTreeVisitor/visitMethod)
* [visitMethodInvocation()](/Java/SimpleTreeVisitor/visitMethodInvocation)
* [visitModifiers()](/Java/SimpleTreeVisitor/visitModifiers)
* [visitNewArray()](/Java/SimpleTreeVisitor/visitNewArray)
* [visitNewClass()](/Java/SimpleTreeVisitor/visitNewClass)
* [visitOther()](/Java/SimpleTreeVisitor/visitOther)
* [visitPackage()](/Java/SimpleTreeVisitor/visitPackage)
* [visitParameterizedType()](/Java/SimpleTreeVisitor/visitParameterizedType)
* [visitParenthesized()](/Java/SimpleTreeVisitor/visitParenthesized)
* [visitPrimitiveType()](/Java/SimpleTreeVisitor/visitPrimitiveType)
* [visitReturn()](/Java/SimpleTreeVisitor/visitReturn)
* [visitSwitch()](/Java/SimpleTreeVisitor/visitSwitch)
* [visitSynchronized()](/Java/SimpleTreeVisitor/visitSynchronized)
* [visitThrow()](/Java/SimpleTreeVisitor/visitThrow)
* [visitTry()](/Java/SimpleTreeVisitor/visitTry)
* [visitTypeCast()](/Java/SimpleTreeVisitor/visitTypeCast)
* [visitTypeParameter()](/Java/SimpleTreeVisitor/visitTypeParameter)
* [visitUnary()](/Java/SimpleTreeVisitor/visitUnary)
* [visitUnionType()](/Java/SimpleTreeVisitor/visitUnionType)
* [visitVariable()](/Java/SimpleTreeVisitor/visitVariable)
* [visitWhileLoop()](/Java/SimpleTreeVisitor/visitWhileLoop)
* [visitWildcard()](/Java/SimpleTreeVisitor/visitWildcard)

## Ejemplo
~~~java
{{ site.data.Java.S.SimpleTreeVisitor.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleTreeVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
