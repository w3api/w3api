---
title: NamingContextOperations.bind_context()
permalink: Java/NamingContextOperations/bind_context
date: 2021-01-04
key: JavaJava.N.NamingContextOperations
category: java
tags: ['java se', 'org.omg.CosNaming', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NamingContextOperations.metodos valor="bind_context" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void bind_context(NameComponent[] n, NamingContext nc) throws NotFound, CannotProceed, InvalidName, AlreadyBound
~~~

## Parámetros
* **NameComponent[] n**,  {% include w3api/param_description.html metodo=_data parametro="NameComponent[] n" %}
* **NamingContext nc**,  {% include w3api/param_description.html metodo=_data parametro="NamingContext nc" %}

## Clase Padre
[NamingContextOperations](/Java/NamingContextOperations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NamingContextOperations.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
