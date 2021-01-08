---
title: AbstractProcessor.getCompletions()
permalink: Java/AbstractProcessor/getCompletions
date: 2021-01-04
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
* **ExecutableElement member**,  {% include w3api/param_description.html metodo=_data parametro="ExecutableElement member" %}
* **AnnotationMirror annotation**,  {% include w3api/param_description.html metodo=_data parametro="AnnotationMirror annotation" %}
* **String userText**,  {% include w3api/param_description.html metodo=_data parametro="String userText" %}
* **Element element**,  {% include w3api/param_description.html metodo=_data parametro="Element element" %}

## Clase Padre
[AbstractProcessor](/Java/AbstractProcessor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractProcessor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
