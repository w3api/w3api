---
title: Activatable.unexportObject()
permalink: Java/Activatable/unexportObject
date: 2021-01-04
key: JavaJava.A.Activatable
category: java
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
* **boolean force**,  {% include w3api/param_description.html metodo=_data parametro="boolean force" %}
* **Remote obj**,  {% include w3api/param_description.html metodo=_data parametro="Remote obj" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[Activatable](/Java/Activatable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Activatable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
