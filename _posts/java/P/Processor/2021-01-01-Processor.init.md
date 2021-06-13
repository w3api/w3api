---
title: Processor.init()
permalink: /Java/Processor/init/
date: 2021-01-11
key: Java.P.Processor
category: Java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Processor.metodos valor="init" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void init(ProcessingEnvironment processingEnv)
~~~

## Parámetros
* **ProcessingEnvironment processingEnv**,  {% include w3api/param_description.html metodo=_dato parametro="ProcessingEnvironment processingEnv" %}

## Clase Padre
[Processor](/Java/Processor/)

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
