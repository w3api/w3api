---
title: ServiceManagerStub.lookup()
permalink: /Java/ServiceManagerStub/lookup/
date: 2021-01-11
key: Java.S.ServiceManagerStub
category: Java
tags: ['java se', 'javax.jnlp', 'java.jnlp', 'metodo java', 'Java 1.4.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceManagerStub.metodos valor="lookup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object lookup(String name) throws UnavailableServiceException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[UnavailableServiceException](/Java/UnavailableServiceException/)

## Clase Padre
[ServiceManagerStub](/Java/ServiceManagerStub/)

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
