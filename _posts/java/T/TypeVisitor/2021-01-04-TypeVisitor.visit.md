---
title: TypeVisitor.visit()
permalink: Java/TypeVisitor/visit
date: 2021-01-04
key: JavaJava.T.TypeVisitor
category: java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeVisitor.metodos valor="visit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default R visit(TypeMirror t)
R visit(TypeMirror t, P p)
~~~

## Parámetros
* **TypeMirror t**,  {% include w3api/param_description.html metodo=_data parametro="TypeMirror t" %}
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}

## Clase Padre
[TypeVisitor](/Java/TypeVisitor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TypeVisitor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
