---
title: AtomicBoolean.lazySet()
permalink: Java/AtomicBoolean/lazySet
date: 2021-01-04
key: JavaJava.A.AtomicBoolean
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicBoolean.metodos valor="lazySet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void lazySet(boolean newValue)
~~~

## Parámetros
* **boolean newValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean newValue" %}

## Clase Padre
[AtomicBoolean](/Java/AtomicBoolean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicBoolean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
