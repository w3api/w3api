---
title: IdentityScope.addIdentity()
permalink: /Java/IdentityScope/addIdentity/
date: 2021-01-11
key: Java.I.IdentityScope
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IdentityScope.metodos valor="addIdentity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void addIdentity(Identity identity) throws KeyManagementException
~~~

## Parámetros
* **Identity identity**,  {% include w3api/param_description.html metodo=_dato parametro="Identity identity" %}

## Excepciones
[KeyManagementException](/Java/KeyManagementException/)

## Clase Padre
[IdentityScope](/Java/IdentityScope/)

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
