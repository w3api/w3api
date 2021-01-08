---
title: MLetMBean.addURL()
permalink: Java/MLetMBean/addURL
date: 2021-01-04
key: JavaJava.M.MLetMBean
category: java
tags: ['java se', 'javax.management.loading', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MLetMBean.metodos valor="addURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addURL(String url) throws ServiceNotFoundException
void addURL(URL url)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **String url**,  {% include w3api/param_description.html metodo=_data parametro="String url" %}

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
{%- for _ldc in site.data.Java.M.MLetMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
