---
title: _NamingContextStub.rebind()
permalink: /Java/_NamingContextStub/rebind/
date: 2021-01-11
key: Java._._NamingContextStub
category: Java
tags: ['java se', 'org.omg.CosNaming', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java._._NamingContextStub.metodos valor="rebind" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void rebind(NameComponent[] n, Object obj) throws NotFound, CannotProceed, InvalidName
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **NameComponent[] n**,  {% include w3api/param_description.html metodo=_dato parametro="NameComponent[] n" %}

## Clase Padre
[_NamingContextStub](/Java/_NamingContextStub/)

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
