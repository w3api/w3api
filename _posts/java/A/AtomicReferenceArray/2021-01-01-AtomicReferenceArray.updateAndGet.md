---
title: AtomicReferenceArray.updateAndGet()
permalink: /Java/AtomicReferenceArray/updateAndGet/
date: 2021-01-11
key: Java.A.AtomicReferenceArray
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceArray.metodos valor="updateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final E updateAndGet(int i, UnaryOperator<E> updateFunction)
~~~

## Parámetros
* **UnaryOperator&lt;E&gt; updateFunction**,  {% include w3api/param_description.html metodo=_dato parametro="UnaryOperator<E> updateFunction" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Clase Padre
[AtomicReferenceArray](/Java/AtomicReferenceArray/)

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
