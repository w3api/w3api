---
title: DynamicLinker.link()
permalink: Java/DynamicLinker/link
date: 2021-01-04
key: JavaJava.D.DynamicLinker
category: java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicLinker.metodos valor="link" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T extends RelinkableCallSite>T link(T callSite)
~~~

## Parámetros
* **T callSite**,  {% include w3api/param_description.html metodo=_data parametro="T callSite" %}

## Clase Padre
[DynamicLinker](/Java/DynamicLinker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DynamicLinker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
