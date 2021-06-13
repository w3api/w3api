---
title: ServiceRegistry.deregisterAll()
permalink: /Java/ServiceRegistry/deregisterAll/
date: 2021-01-11
key: Java.S.ServiceRegistry
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="deregisterAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void deregisterAll()
public void deregisterAll(Class<?> category)
~~~

## Parámetros
* **Class&lt;?&gt; category**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> category" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ServiceRegistry](/Java/ServiceRegistry/)

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
