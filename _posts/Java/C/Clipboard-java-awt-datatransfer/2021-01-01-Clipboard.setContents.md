---
title: Clipboard.setContents()
permalink: /Java/Clipboard-java-awt-datatransfer/setContents/
date: 2021-01-11
key: Java.C.Clipboard-java-awt-datatransfer
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Clipboard-java-awt-datatransfer.metodos valor="setContents" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setContents(Transferable contents, ClipboardOwner owner)
~~~

## Parámetros
* **Transferable contents**,  {% include w3api/param_description.html metodo=_dato parametro="Transferable contents" %}
* **ClipboardOwner owner**,  {% include w3api/param_description.html metodo=_dato parametro="ClipboardOwner owner" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[Clipboard](/Java/Clipboard-java-awt-datatransfer/)

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
