---
title: RemoteStub.setRef()
permalink: Java/RemoteStub/setRef
date: 2021-01-11
key: JavaJava.R.RemoteStub
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteStub.metodos valor="setRef" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated protected static void setRef(RemoteStub stub, RemoteRef ref)
~~~

## Parámetros
* **RemoteStub stub**,  {% include w3api/param_description.html metodo=_dato parametro="RemoteStub stub" %}
* **RemoteRef ref**,  {% include w3api/param_description.html metodo=_dato parametro="RemoteRef ref" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[RemoteStub](/Java/RemoteStub/)

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
