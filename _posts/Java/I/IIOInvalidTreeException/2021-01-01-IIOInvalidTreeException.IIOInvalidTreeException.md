---
title: IIOInvalidTreeException.IIOInvalidTreeException()
permalink: /Java/IIOInvalidTreeException/IIOInvalidTreeException/
date: 2021-01-11
key: Java.I.IIOInvalidTreeException
category: Java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOInvalidTreeException.constructores valor="IIOInvalidTreeException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IIOInvalidTreeException(String message, Throwable cause, Node offendingNode)
public IIOInvalidTreeException(String message, Node offendingNode)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **Node offendingNode**,  {% include w3api/param_description.html metodo=_dato parametro="Node offendingNode" %}

## Clase Padre
[IIOInvalidTreeException](/Java/IIOInvalidTreeException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
