---
title: AnnotationValueVisitor.visitArray()
permalink: /Java/AnnotationValueVisitor/visitArray/
date: 2021-01-11
key: Java.A.AnnotationValueVisitor
category: Java
tags: ['java se', 'javax.lang.model.element', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AnnotationValueVisitor.metodos valor="visitArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitArray(List<? extends AnnotationValue> vals, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **List&lt;? extends AnnotationValue&gt; vals**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends AnnotationValue> vals" %}

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
