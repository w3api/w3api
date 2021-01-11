---
title: AbstractProcessor.getCompletions()
permalink: Java/AbstractProcessor/getCompletions
date: 2021-01-10
key: JavaJava.A.AbstractProcessor
category: java
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
* **Element element**,  {% include w3api/param_description.html metodo=_dato parametro="Element element" %}
* **ExecutableElement member**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutableElement member" %}
* **AnnotationMirror annotation**,  {% include w3api/param_description.html metodo=_dato parametro="AnnotationMirror annotation" %}
* **String userText**,  {% include w3api/param_description.html metodo=_dato parametro="String userText" %}

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
