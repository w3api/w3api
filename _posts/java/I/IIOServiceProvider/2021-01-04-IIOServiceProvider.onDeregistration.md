---
title: IIOServiceProvider.onDeregistration()
permalink: Java/IIOServiceProvider/onDeregistration
date: 2021-01-04
key: JavaJava.I.IIOServiceProvider
category: java
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
* **ServiceRegistry registry**,  {% include w3api/param_description.html metodo=_data parametro="ServiceRegistry registry" %}
* **Class&lt;?&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> category" %}

## Clase Padre
[IIOServiceProvider](/Java/IIOServiceProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOServiceProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
