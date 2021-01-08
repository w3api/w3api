---
title: _NamingContextStub.bind_context()
permalink: Java/_NamingContextStub/bind_context
date: 2021-01-04
key: JavaJava._._NamingContextStub
category: java
tags: ['java se', 'org.omg.CosNaming', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java._._NamingContextStub.metodos valor="bind_context" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void bind_context(NameComponent[] n, NamingContext nc) throws NotFound, CannotProceed, InvalidName, AlreadyBound
~~~

## Parámetros
* **NameComponent[] n**,  {% include w3api/param_description.html metodo=_data parametro="NameComponent[] n" %}
* **NamingContext nc**,  {% include w3api/param_description.html metodo=_data parametro="NamingContext nc" %}

## Clase Padre
[_NamingContextStub](/Java/_NamingContextStub/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java._._NamingContextStub.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
