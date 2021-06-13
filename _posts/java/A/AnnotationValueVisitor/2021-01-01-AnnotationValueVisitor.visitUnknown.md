---
title: AnnotationValueVisitor.visitUnknown()
permalink: /Java/AnnotationValueVisitor/visitUnknown/
date: 2021-01-11
key: Java.A.AnnotationValueVisitor
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotationValueVisitor.metodos valor="visitUnknown" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitUnknown(AnnotationValue av, P p)
~~~

## Parámetros
* **AnnotationValue av**,  {% include w3api/param_description.html metodo=_dato parametro="AnnotationValue av" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Excepciones
[UnknownAnnotationValueException](/Java/UnknownAnnotationValueException/)

## Clase Padre
[AnnotationValueVisitor](/Java/AnnotationValueVisitor/)

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
