---
title: Activatable.unexportObject()
permalink: /Java/Activatable/unexportObject/
date: 2021-01-11
key: Java.A.Activatable
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activatable.metodos valor="unexportObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean unexportObject(Remote obj, boolean force) throws NoSuchObjectException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}
* **boolean force**,  {% include w3api/param_description.html metodo=_dato parametro="boolean force" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Activatable](/Java/Activatable/)

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
