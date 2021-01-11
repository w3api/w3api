---
title: AtomicReferenceArray.weakCompareAndSetPlain()
permalink: Java/AtomicReferenceArray/weakCompareAndSetPlain
date: 2021-01-11
key: JavaJava.A.AtomicReferenceArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceArray.metodos valor="weakCompareAndSetPlain" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean weakCompareAndSetPlain(int i, E expectedValue, E newValue)
~~~

## Parámetros
* **E newValue**,  {% include w3api/param_description.html metodo=_dato parametro="E newValue" %}
* **E expectedValue**,  {% include w3api/param_description.html metodo=_dato parametro="E expectedValue" %}
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
