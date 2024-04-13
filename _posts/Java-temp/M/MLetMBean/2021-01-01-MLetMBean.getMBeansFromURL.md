---
title: MLetMBean.getMBeansFromURL()
permalink: /Java/MLetMBean/getMBeansFromURL/
date: 2021-01-11
key: Java.M.MLetMBean
category: Java
tags: ['java se', 'javax.management.loading', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MLetMBean.metodos valor="getMBeansFromURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Set<Object> getMBeansFromURL(String url) throws ServiceNotFoundException
Set<Object> getMBeansFromURL(URL url) throws ServiceNotFoundException
~~~

## Parámetros
* **String url**,  {% include w3api/param_description.html metodo=_dato parametro="String url" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}

## Excepciones
[ServiceNotFoundException](/Java/ServiceNotFoundException/)

## Clase Padre
[MLetMBean](/Java/MLetMBean/)

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
