---
title: DynamicLinker.link()
permalink: /Java/DynamicLinker/link/
date: 2021-01-11
key: Java.D.DynamicLinker
category: Java
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
* **T callSite**,  {% include w3api/param_description.html metodo=_dato parametro="T callSite" %}

## Clase Padre
[DynamicLinker](/Java/DynamicLinker/)

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
