---
title: ServiceRegistry.getServiceProviderByClass()
permalink: Java/ServiceRegistry/getServiceProviderByClass
date: 2021-01-11
key: JavaJava.S.ServiceRegistry
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="getServiceProviderByClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T getServiceProviderByClass(Class<T> providerClass)
~~~

## Parámetros
* **Class&lt;T&gt; providerClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> providerClass" %}

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
