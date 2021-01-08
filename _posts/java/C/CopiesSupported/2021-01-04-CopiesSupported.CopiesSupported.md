---
title: CopiesSupported.CopiesSupported()
permalink: Java/CopiesSupported/CopiesSupported
date: 2021-01-04
key: JavaJava.C.CopiesSupported
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CopiesSupported.constructores valor="CopiesSupported" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CopiesSupported(int member)
public CopiesSupported(int lowerBound, int upperBound)
~~~

## Parámetros
* **int upperBound**,  {% include w3api/param_description.html metodo=_data parametro="int upperBound" %}
* **int member**,  {% include w3api/param_description.html metodo=_data parametro="int member" %}
* **int lowerBound**,  {% include w3api/param_description.html metodo=_data parametro="int lowerBound" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CopiesSupported](/Java/CopiesSupported/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CopiesSupported.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
