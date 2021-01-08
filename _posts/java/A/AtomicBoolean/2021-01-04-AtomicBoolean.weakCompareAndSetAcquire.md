---
title: AtomicBoolean.weakCompareAndSetAcquire()
permalink: Java/AtomicBoolean/weakCompareAndSetAcquire
date: 2021-01-04
key: JavaJava.A.AtomicBoolean
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicBoolean.metodos valor="weakCompareAndSetAcquire" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final boolean weakCompareAndSetAcquire(boolean expectedValue, boolean newValue)
~~~

## Parámetros
* **boolean newValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean newValue" %}
* **boolean expectedValue**,  {% include w3api/param_description.html metodo=_data parametro="boolean expectedValue" %}

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
