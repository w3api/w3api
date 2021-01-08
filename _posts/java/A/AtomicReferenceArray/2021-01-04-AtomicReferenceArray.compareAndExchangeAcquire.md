---
title: AtomicReferenceArray.compareAndExchangeAcquire()
permalink: Java/AtomicReferenceArray/compareAndExchangeAcquire
date: 2021-01-04
key: JavaJava.A.AtomicReferenceArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicReferenceArray.metodos valor="compareAndExchangeAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final E compareAndExchangeAcquire(int i, E expectedValue, E newValue)
~~~

## Parámetros
* **E expectedValue**,  {% include w3api/param_description.html metodo=_data parametro="E expectedValue" %}
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **E newValue**,  {% include w3api/param_description.html metodo=_data parametro="E newValue" %}

## Clase Padre
[AtomicReferenceArray](/Java/AtomicReferenceArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicReferenceArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
