---
title: IIOServiceProvider.onRegistration()
permalink: Java/IIOServiceProvider/onRegistration
date: 2021-01-11
key: JavaJava.I.IIOServiceProvider
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOServiceProvider.metodos valor="onRegistration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void onRegistration(ServiceRegistry registry, Class<?> category)
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
