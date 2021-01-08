---
title: MessageContext.setScope()
permalink: Java/MessageContext/setScope
date: 2021-01-04
key: JavaJava.M.MessageContext
category: java
tags: ['java se', 'javax.xml.ws.handler', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MessageContext.metodos valor="setScope" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setScope(String name, MessageContext.Scope scope)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **MessageContext.Scope scope**,  {% include w3api/param_description.html metodo=_data parametro="MessageContext.Scope scope" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MessageContext](/Java/MessageContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MessageContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
