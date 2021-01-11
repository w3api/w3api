---
title: Unmarshaller.unmarshal()
permalink: Java/Unmarshaller/unmarshal
date: 2021-01-11
key: JavaJava.U.Unmarshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Unmarshaller.metodos valor="unmarshal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object unmarshal(File f) throws JAXBException
Object unmarshal(InputStream is) throws JAXBException
Object unmarshal(Reader reader) throws JAXBException
Object unmarshal(URL url) throws JAXBException
Object unmarshal(XMLEventReader reader) throws JAXBException
<T> JAXBElement<T> unmarshal(XMLEventReader reader, Class<T> declaredType)
Object unmarshal(XMLStreamReader reader) throws JAXBException
<T> JAXBElement<T> unmarshal(XMLStreamReader reader, Class<T> declaredType)
Object unmarshal(Source source) throws JAXBException
<T> JAXBElement<T> unmarshal(Source source, Class<T> declaredType)
Object unmarshal(Node node) throws JAXBException
<T> JAXBElement<T> unmarshal(Node node, Class<T> declaredType)
Object unmarshal(InputSource source) throws JAXBException
~~~

## Parámetros
* **File f**,  {% include w3api/param_description.html metodo=_dato parametro="File f" %}
* **Source source**,  {% include w3api/param_description.html metodo=_dato parametro="Source source" %}
* **XMLStreamReader reader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStreamReader reader" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **InputStream is**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream is" %}
* **XMLEventReader reader**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEventReader reader" %}
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}
* **InputSource source**,  {% include w3api/param_description.html metodo=_dato parametro="InputSource source" %}
* **Class&lt;T&gt; declaredType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> declaredType" %}

## Excepciones
[UnmarshalException](/Java/UnmarshalException/), [JAXBException](/Java/JAXBException/), [IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Unmarshaller](/Java/Unmarshaller/)

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
