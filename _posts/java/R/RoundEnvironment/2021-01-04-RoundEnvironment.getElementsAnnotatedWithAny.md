---
title: RoundEnvironment.getElementsAnnotatedWithAny()
permalink: Java/RoundEnvironment/getElementsAnnotatedWithAny
date: 2021-01-04
key: JavaJava.R.RoundEnvironment
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RoundEnvironment.metodos valor="getElementsAnnotatedWithAny" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Set<? extends Element> getElementsAnnotatedWithAny(Set<Class<? extends Annotation>> annotations)
default Set<? extends Element> getElementsAnnotatedWithAny(TypeElement... annotations)
~~~

## Parámetros
* **TypeElement... annotations**,  {% include w3api/param_description.html metodo=_data parametro="TypeElement... annotations" %}
* **Set&lt;Class&lt;? extends Annotation&gt;&gt; annotations**,  {% include w3api/param_description.html metodo=_data parametro="Set<Class<? extends Annotation>> annotations" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[RoundEnvironment](/Java/RoundEnvironment/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RoundEnvironment.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
