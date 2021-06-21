---
title: ClipboardOwner.lostOwnership()
permalink: /Java/ClipboardOwner/lostOwnership/
date: 2021-01-11
key: Java.C.ClipboardOwner
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClipboardOwner.metodos valor="lostOwnership" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void lostOwnership(Clipboard clipboard, Transferable contents)
~~~

## Parámetros
* **Transferable contents**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable contents" %}
* **Clipboard clipboard**,  {% include w3api/param_description.html metodo=_dato parametro="Clipboard clipboard" %}

## Clase Padre
[ClipboardOwner](/Java/ClipboardOwner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
