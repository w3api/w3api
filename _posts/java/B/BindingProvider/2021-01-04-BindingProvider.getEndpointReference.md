---
title: BindingProvider.getEndpointReference()
permalink: Java/BindingProvider/getEndpointReference
date: 2021-01-04
key: JavaJava.B.BindingProvider
category: java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BindingProvider.metodos valor="getEndpointReference" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
EndpointReference getEndpointReference()
<T extends EndpointReference>T getEndpointReference(Class<T> clazz)
~~~

## Parámetros
* **Class&lt;T&gt; clazz**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> clazz" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[BindingProvider](/Java/BindingProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BindingProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
