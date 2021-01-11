---
title: AbstractProcessor.init()
permalink: Java/AbstractProcessor/init
date: 2021-01-10
key: JavaJava.A.AbstractProcessor
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractProcessor.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void init(ProcessingEnvironment processingEnv)
~~~

## Parámetros
* **ProcessingEnvironment processingEnv**,  {% include w3api/param_description.html metodo=_dato parametro="ProcessingEnvironment processingEnv" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

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
