---
title: InitialContext.composeName()
permalink: Java/InitialContext/composeName
date: 2021-01-04
key: JavaJava.I.InitialContext
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3', 'JNDI Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InitialContext.metodos valor="composeName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String composeName(String name, String prefix) throws NamingException
public Name composeName(Name name, Name prefix) throws NamingException
~~~

## Parámetros
* **Name prefix**,  {% include w3api/param_description.html metodo=_data parametro="Name prefix" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

## Excepciones
[NamingException](/Java/NamingException/)

## Clase Padre
[InitialContext](/Java/InitialContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InitialContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
