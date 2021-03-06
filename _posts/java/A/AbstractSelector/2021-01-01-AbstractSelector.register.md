---
title: AbstractSelector.register()
permalink: /Java/AbstractSelector/register/
date: 2021-01-11
key: Java.A.AbstractSelector
category: Java
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
* **Object att**,  {% include w3api/param_description.html metodo=_dato parametro="Object att" %}
* **int ops**,  {% include w3api/param_description.html metodo=_dato parametro="int ops" %}
* **AbstractSelectableChannel ch**,  {% include w3api/param_description.html metodo=_dato parametro="AbstractSelectableChannel ch" %}

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
