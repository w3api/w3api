---
title: AbstractProcessor.getCompletions()
permalink: /Java/AbstractProcessor/getCompletions/
date: 2021-01-11
key: Java.A.AbstractProcessor
category: Java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractProcessor.metodos valor="getCompletions" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Iterable<? extends Completion> getCompletions(Element element, AnnotationMirror annotation, ExecutableElement member, String userText)
~~~

## Parámetros
* **AnnotationMirror annotation**,  {% include w3api/param_description.html metodo=_dato parametro="AnnotationMirror annotation" %}
* **Element element**,  {% include w3api/param_description.html metodo=_dato parametro="Element element" %}
* **String userText**,  {% include w3api/param_description.html metodo=_dato parametro="String userText" %}
* **ExecutableElement member**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutableElement member" %}

## Clase Padre
[AbstractProcessor](/Java/AbstractProcessor/)

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
