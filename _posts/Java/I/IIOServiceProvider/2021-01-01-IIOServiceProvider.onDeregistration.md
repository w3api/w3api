---
title: IIOServiceProvider.onDeregistration()
permalink: /Java/IIOServiceProvider/onDeregistration/
date: 2021-01-11
key: Java.I.IIOServiceProvider
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOServiceProvider.metodos valor="onDeregistration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void onDeregistration(ServiceRegistry registry, Class<?> category)
~~~

## Parámetros
* **ServiceRegistry registry**,  {% include w3api/param_description.html metodo=_dato parametro="ServiceRegistry registry" %}
* **Class&lt;?&gt; category**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> category" %}

## Clase Padre
[IIOServiceProvider](/Java/IIOServiceProvider/)

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
