---
title: SimpleTreeVisitor.visitLambdaExpression()
permalink: Java/SimpleTreeVisitor/visitLambdaExpression
date: 2021-01-04
key: JavaJava.S.SimpleTreeVisitor
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTreeVisitor.metodos valor="visitLambdaExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitLambdaExpression(LambdaExpressionTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **LambdaExpressionTree node**,  {% include w3api/param_description.html metodo=_data parametro="LambdaExpressionTree node" %}

## Clase Padre
[SimpleTreeVisitor](/Java/SimpleTreeVisitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SimpleTreeVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
