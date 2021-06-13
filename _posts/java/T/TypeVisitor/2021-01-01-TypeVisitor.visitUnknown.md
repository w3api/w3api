---
title: TypeVisitor.visitUnknown()
permalink: /Java/TypeVisitor/visitUnknown/
date: 2021-01-11
key: Java.T.TypeVisitor
category: Java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeVisitor.metodos valor="visitUnknown" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitUnknown(TypeMirror t, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **TypeMirror t**,  {% include w3api/param_description.html metodo=_dato parametro="TypeMirror t" %}

## Excepciones
[UnknownTypeException](/Java/UnknownTypeException/)

## Clase Padre
[TypeVisitor](/Java/TypeVisitor/)

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
