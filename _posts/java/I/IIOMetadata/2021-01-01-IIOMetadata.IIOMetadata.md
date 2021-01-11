---
title: IIOMetadata.IIOMetadata()
permalink: Java/IIOMetadata/IIOMetadata
date: 2021-01-11
key: JavaJava.I.IIOMetadata
category: java
tags: ['java se', 'javax.imageio.metadata', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOMetadata.constructores valor="IIOMetadata" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected IIOMetadata()
protected IIOMetadata(boolean standardMetadataFormatSupported, String nativeMetadataFormatName, String nativeMetadataFormatClassName, String[] extraMetadataFormatNames, String[] extraMetadataFormatClassNames)
~~~

## Parámetros
* **String[] extraMetadataFormatNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraMetadataFormatNames" %}
* **String nativeMetadataFormatName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeMetadataFormatName" %}
* **boolean standardMetadataFormatSupported**,  {% include w3api/param_description.html metodo=_dato parametro="boolean standardMetadataFormatSupported" %}
* **String nativeMetadataFormatClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String nativeMetadataFormatClassName" %}
* **String[] extraMetadataFormatClassNames**,  {% include w3api/param_description.html metodo=_dato parametro="String[] extraMetadataFormatClassNames" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[IIOMetadata](/Java/IIOMetadata/)

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
