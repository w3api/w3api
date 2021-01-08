---
title: AbstractSelector.register()
permalink: Java/AbstractSelector/register
date: 2021-01-04
key: JavaJava.A.AbstractSelector
category: java
tags: ['java se', 'java.nio.channels.spi', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSelector.metodos valor="register" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract SelectionKey register(AbstractSelectableChannel ch, int ops, Object att)
~~~

## Parámetros
* **int ops**,  {% include w3api/param_description.html metodo=_data parametro="int ops" %}
* **AbstractSelectableChannel ch**,  {% include w3api/param_description.html metodo=_data parametro="AbstractSelectableChannel ch" %}
* **Object att**,  {% include w3api/param_description.html metodo=_data parametro="Object att" %}

## Clase Padre
[AbstractSelector](/Java/AbstractSelector/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractSelector.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
