---
title: Processor.process()
permalink: Java/Processor/process
date: 2021-01-04
key: JavaJava.P.Processor
category: java
tags: ['java se', 'javax.annotation.processing', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Processor.metodos valor="process" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean process(Set<? extends TypeElement> annotations, RoundEnvironment roundEnv)
~~~

## Parámetros
* **Set&lt;? extends TypeElement&gt; annotations**,  {% include w3api/param_description.html metodo=_data parametro="Set<? extends TypeElement> annotations" %}
* **RoundEnvironment roundEnv**,  {% include w3api/param_description.html metodo=_data parametro="RoundEnvironment roundEnv" %}

## Clase Padre
[Processor](/Java/Processor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.Processor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
