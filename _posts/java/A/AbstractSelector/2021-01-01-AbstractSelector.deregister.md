---
title: AbstractSelector.deregister()
permalink: Java/AbstractSelector/deregister
date: 2021-01-11
key: JavaJava.A.AbstractSelector
category: java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSelector.metodos valor="deregister" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void deregister(AbstractSelectionKey key)
~~~

## Parámetros
* **AbstractSelectionKey key**,  {% include w3api/param_description.html metodo=_dato parametro="AbstractSelectionKey key" %}

## Clase Padre
[AbstractSelector](/Java/AbstractSelector/)

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
