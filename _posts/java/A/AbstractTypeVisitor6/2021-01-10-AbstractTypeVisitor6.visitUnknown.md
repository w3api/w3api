---
title: AbstractTypeVisitor6.visitUnknown()
permalink: Java/AbstractTypeVisitor6/visitUnknown
date: 2021-01-10
key: JavaJava.A.AbstractTypeVisitor6
category: java
tags: ['java se', 'javax.lang.model.util', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractTypeVisitor6.metodos valor="visitUnknown" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitUnknown(TypeMirror t, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **TypeMirror t**,  {% include w3api/param_description.html metodo=_dato parametro="TypeMirror t" %}

## Excepciones
[UnknownTypeException](/Java/UnknownTypeException/)

## Clase Padre
[AbstractTypeVisitor6](/Java/AbstractTypeVisitor6/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
