---
title: InheritableThreadLocal.childValue()
permalink: Java/InheritableThreadLocal/childValue
date: 2021-01-04
key: JavaJava.I.InheritableThreadLocal
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InheritableThreadLocal.metodos valor="childValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected T childValue(T parentValue)
~~~

## Parámetros
* **T parentValue**,  {% include w3api/param_description.html metodo=_data parametro="T parentValue" %}

## Clase Padre
[InheritableThreadLocal](/Java/InheritableThreadLocal/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InheritableThreadLocal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
