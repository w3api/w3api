---
title: MulticastSocket.setLoopbackMode()
permalink: /Java/MulticastSocket/setLoopbackMode/
date: 2021-01-11
key: Java.M.MulticastSocket
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MulticastSocket.metodos valor="setLoopbackMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setLoopbackMode(boolean disable) throws SocketException
~~~

## Parámetros
* **boolean disable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean disable" %}

## Excepciones
[SocketException](/Java/SocketException/)

## Clase Padre
[MulticastSocket](/Java/MulticastSocket/)

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
