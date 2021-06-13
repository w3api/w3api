---
title: AtomicReference.updateAndGet()
permalink: /Java/AtomicReference/updateAndGet/
date: 2021-01-11
key: Java.A.AtomicReference
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReference.metodos valor="updateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final V updateAndGet(UnaryOperator<V> updateFunction)
~~~

## Parámetros
* **UnaryOperator&lt;V&gt; updateFunction**,  {% include w3api/param_description.html metodo=_dato parametro="UnaryOperator<V> updateFunction" %}

## Clase Padre
[AtomicReference](/Java/AtomicReference/)

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
